
#include <AzCore/Serialization/SerializeContext.h>
#include <InteractiveTutorialsEditorSystemComponent.h>

namespace InteractiveTutorials
{
    void InteractiveTutorialsEditorSystemComponent::Reflect(AZ::ReflectContext* context)
    {
        if (auto serializeContext = azrtti_cast<AZ::SerializeContext*>(context))
        {
            serializeContext->Class<InteractiveTutorialsEditorSystemComponent, AZ::Component>();
        }
    }

    InteractiveTutorialsEditorSystemComponent::InteractiveTutorialsEditorSystemComponent()
    {
        if (InteractiveTutorialsInterface::Get() == nullptr)
        {
            InteractiveTutorialsInterface::Register(this);
        }
    }

    InteractiveTutorialsEditorSystemComponent::~InteractiveTutorialsEditorSystemComponent()
    {
        if (InteractiveTutorialsInterface::Get() == this)
        {
            InteractiveTutorialsInterface::Unregister(this);
        }
    }

    void InteractiveTutorialsEditorSystemComponent::GetProvidedServices(AZ::ComponentDescriptor::DependencyArrayType& provided)
    {
        provided.push_back(AZ_CRC_CE("InteractiveTutorialsEditorService"));
    }

    void InteractiveTutorialsEditorSystemComponent::GetIncompatibleServices(AZ::ComponentDescriptor::DependencyArrayType& incompatible)
    {
        incompatible.push_back(AZ_CRC_CE("InteractiveTutorialsEditorService"));
    }

    void InteractiveTutorialsEditorSystemComponent::GetRequiredServices([[maybe_unused]] AZ::ComponentDescriptor::DependencyArrayType& required)
    {
    }

    void InteractiveTutorialsEditorSystemComponent::GetDependentServices([[maybe_unused]] AZ::ComponentDescriptor::DependencyArrayType& dependent)
    {
    }

    void InteractiveTutorialsEditorSystemComponent::Activate()
    {
        InteractiveTutorialsRequestBus::Handler::BusConnect();
        AzToolsFramework::EditorEvents::Bus::Handler::BusConnect();
    }

    void InteractiveTutorialsEditorSystemComponent::Deactivate()
    {
        AzToolsFramework::EditorEvents::Bus::Handler::BusDisconnect();
        InteractiveTutorialsRequestBus::Handler::BusDisconnect();
    }

} // namespace InteractiveTutorials
