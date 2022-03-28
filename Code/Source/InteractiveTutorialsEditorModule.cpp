
#include <InteractiveTutorialsModuleInterface.h>
#include <InteractiveTutorialsEditorSystemComponent.h>
#include <AzToolsFramework/API/PythonLoader.h>

void InitInteractiveTutorialsResources()
{
    // We must register our Qt resources (.qrc file) since this is being loaded from a separate module (gem)
    Q_INIT_RESOURCE(InteractiveTutorials);
}

namespace InteractiveTutorials
{
    class InteractiveTutorialsEditorModule
        : public InteractiveTutorialsModuleInterface
        , public AzToolsFramework::EmbeddedPython::PythonLoader
    {
    public:
        AZ_RTTI(InteractiveTutorialsEditorModule, "{c00dc88a-61e8-4b45-9651-b0c8e8dcbf37}", InteractiveTutorialsModuleInterface);
        AZ_CLASS_ALLOCATOR(InteractiveTutorialsEditorModule, AZ::SystemAllocator, 0);

        InteractiveTutorialsEditorModule()
        {
            InitInteractiveTutorialsResources();

            // Push results of [MyComponent]::CreateDescriptor() into m_descriptors here.
            // Add ALL components descriptors associated with this gem to m_descriptors.
            // This will associate the AzTypeInfo information for the components with the the SerializeContext, BehaviorContext and EditContext.
            // This happens through the [MyComponent]::Reflect() function.
            m_descriptors.insert(m_descriptors.end(), {
                InteractiveTutorialsEditorSystemComponent::CreateDescriptor(),
            });
        }

        /**
         * Add required SystemComponents to the SystemEntity.
         * Non-SystemComponents should not be added here
         */
        AZ::ComponentTypeList GetRequiredSystemComponents() const override
        {
            return AZ::ComponentTypeList {
                azrtti_typeid<InteractiveTutorialsEditorSystemComponent>(),
            };
        }
    };
}// namespace InteractiveTutorials

AZ_DECLARE_MODULE_CLASS(Gem_InteractiveTutorials, InteractiveTutorials::InteractiveTutorialsEditorModule)
