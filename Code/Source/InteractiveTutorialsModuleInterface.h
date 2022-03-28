
#include <AzCore/Memory/SystemAllocator.h>
#include <AzCore/Module/Module.h>

namespace InteractiveTutorials
{
    class InteractiveTutorialsModuleInterface
        : public AZ::Module
    {
    public:
        AZ_RTTI(InteractiveTutorialsModuleInterface, "{50442670-b927-4f25-b5c1-b4c7db21b766}", AZ::Module);
        AZ_CLASS_ALLOCATOR(InteractiveTutorialsModuleInterface, AZ::SystemAllocator, 0);

        InteractiveTutorialsModuleInterface()
        {
        }

        /**
         * Add required SystemComponents to the SystemEntity.
         */
        AZ::ComponentTypeList GetRequiredSystemComponents() const override
        {
            return AZ::ComponentTypeList{
            };
        }
    };
}// namespace InteractiveTutorials
